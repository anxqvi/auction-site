<template>
    <p>Profile</p>
    

    <form @submit.prevent="editProfile">
        <div>
            <label>Date of Birth:</label><br>
            <input type="date" name="dob" v-model="user.dob"><br>
            <label>Email:</label><br>
            <input type="email" name="email" v-model="user.email"><br>
            <button type="submit">Submit</button>
        </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
           user: {} 
        }
    },
    mounted() {
        this.getUser()
    },
    methods: {
        async getUser() {
            let response = await fetch(
                "http://localhost:8000/api/user/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
        let data = await response.json();
        this.user = data.user;
        },

        async fetchProfile() {
            let response = await fetch(
                "http://localhost:8000/api/profile/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
        let data = await response.json();
        this.user = data.user;
        },

        async editProfile() {
            let response = await fetch("http://localhost:8000/api/profile/", 
            {
                method: "put",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.user)
            }
            );
            let data = await response.json();
            this.user = data.user;
        },
    }
}
</script>