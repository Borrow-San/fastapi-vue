import torch
from transformers import PreTrainedTokenizerFast

Q_TKN = "<usr>"
A_TKN = "<sys>"
BOS = '</s>'
EOS = '</s>'
MASK = '<unused0>'
SENT = '<unused1>'
PAD = '<pad>'

def chat_test(text):
    koGPT2_TOKENIZER = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2", bos_token=BOS, eos_token=EOS,
                                                               unk_token="<unk>", pad_token=PAD, mask_token=MASK, )
    model = torch.load("./bs_chat.pt")
    with torch.no_grad():
        while 1:
            if text == "quit":
                break
            a = ""
            while 1:
                input_ids = torch.LongTensor(koGPT2_TOKENIZER.encode(Q_TKN + text + SENT + A_TKN + a)).unsqueeze(dim=0)
                model.to('cpu')
                pred = model(input_ids)
                pred = pred.logits
                gen = koGPT2_TOKENIZER.convert_ids_to_tokens(torch.argmax(pred, dim=-1).squeeze().numpy().tolist())[-1]
                if gen == EOS:
                    break
                a += gen.replace("▁", " ")
        return a.strip()
