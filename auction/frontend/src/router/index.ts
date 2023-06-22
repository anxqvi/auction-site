import {createRouter, createWebHistory} from 'vue-router'
import Auction from '../views/Auction.vue'
import Home from '../views/Home.vue'
import Profile from '../views/Profile.vue'
import Bid from '../views/Bid.vue'

const routes = [
    {path: '/', name: 'Home', component: Home},
    {path: '/auction', name: 'Auction', component: Auction},
    {path: '/profile', name: 'Profile', component: Profile},
    {path: '/bid-detail/:item_id', name: 'Bid', component: Bid}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router