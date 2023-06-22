<template>
    <div class="nav">
        <router-link to="/">Home</router-link>
        <router-link to="/auction">Auction</router-link>
        <router-link to="/profile">Profile</router-link>
        <router-link to="/bid-detail">Bid</router-link>

        <form class="search-container" @submit.prevent=searchItems>
            <div>
                <input class="input" type="text" v-model="searchText" placeholder="Search">
                <button class="action-text" type="search">Search</button>
            </div>
        </form>
    </div>

    <div>
        <router-view></router-view>
    </div>
</template>



<script>
export default {
    methods: {
        async searchItems() {
            let response = await fetch('http://localhost:8000/api/search/', 
            {
                method: "post",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.searchText)
            }
            );
            let data= await response.json();
            this.items = data.items
        }
    }
}
</script>


