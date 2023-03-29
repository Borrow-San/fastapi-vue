import { createRouter, createWebHistory} from 'vue-router'
 
import InfoMain from '@/views/InfoMain.vue'
import LoginPage from '@/views/LoginPage.vue'
import AdminPage from '@/views/AdminPage.vue'

import AdminMain from '@/components/admin/AdminMain.vue'
import UserInfo from '@/components/admin/UserInfo.vue'
import AdminInfo from '@/components/admin/InfoAdmin.vue'
import AdminCreate from '@/components/admin/CreateAdmin.vue'
import AdminDelete from '@/components/admin/DeleteAdmin.vue'
import ArticleInfo from '@/components/article/InfoArticle.vue'
import ArticleCreate from '@/components/article/CreateArticle.vue'
import ArticleDelete from '@/components/article/DeleteArticle.vue'
import ArticleClame from '@/components/article/ClaimArticle.vue'


const routes = [
    {
        path: '/',
        component: InfoMain
    },
    {
        path: '/login',
        component: LoginPage
    },
    {
        path: '/admin',
        component: AdminPage,
        children: [
            { path: '', component: AdminMain },
            { path: 'admin-info', component: AdminInfo },
            { path: 'admin-create', component: AdminCreate },
            { path: 'admin-delete', component: AdminDelete },
            { path: 'article-info', component: ArticleInfo },
            { path: 'article-create', component: ArticleCreate },
            { path: 'article-delete', component: ArticleDelete },
            { path: 'article-clame', component: ArticleClame },
            { path: 'user-info', component: UserInfo }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(process.env.VUE_APP_FRONTEND_URL),
    routes
})

export { router }