import { createRouter, createWebHistory} from 'vue-router'
 
import InfoMain from '@/views/InfoMain.vue'
import LoginPage from '@/views/LoginPage.vue'
import AdminPage from '@/views/AdminPage.vue'

import AdminMain from '@/components/admin/AdminMain.vue'
import AdminInfo from '@/components/admin/AdminInfo.vue'
import AdminCreate from '@/components/admin/AdminCreate.vue'
import AdminDelete from '@/components/admin/AdminDelete.vue'
import ArticleInfo from '@/components/article/ArticleInfo.vue'
import ArticleCreate from '@/components/article/ArticleCreate.vue'
import ArticleDelete from '@/components/article/ArticleDelete.vue'
import ArticleClame from '@/components/article/ArticleClaims.vue'


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
            { path: 'article-clame', component: ArticleClame }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export { router }