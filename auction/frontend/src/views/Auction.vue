<template>

    <form @submit.prevent="addItem">
        <div>
            <label>Title:</label><br>
            <input type="text" name="title" v-model="item.title"><br>
            <label>Starting Price:</label><br>
            <input type="number" step="0.01" name="starting_price" v-model="item.starting_price"><br>
            <label>Description:</label><br>
            <input type="text" name="description" v-model="item.description"><br>
            <label>End Date</label><br>
            <input type="date" name="end_date" v-model="item.end_date"><br>
            <label>End Time:</label><br>
            <input type="time" name="end_time" v-model="item.end_time"><br>
            <button type="submit">Submit</button>
        </div>
    </form>

    
</template>

<script>
export default {
    data() {
        return {
            item: {},
            questions: [],
            answers: [],
            question: {},
            answer: {},
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
    },
    async addItem() {
            let response = await fetch("http://localhost:8000/api/items/", 
            {
                method: "post",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.item)
            }
            );
            let data = await response.json();
            this.item = data.item;
        },
}
</script>