<template>
    <div>
        <div class="title">
            <h1>Welcome to the Auction!</h1>
        </div>
        
        <div class="container">
            <div class="item-box" v-for="item in items" v-bind:key="item.id">
                <figure class="item-image">
                    <img v-bind:src="sliceString(item.item_image)" id="item_pic"/>
                </figure>

                <div class="item-info">
                    <span class="item-title">{{item.title}}<br></span>
                    <span class="item-price">Starting Price: £{{item.starting_price}}<br></span>
                    <span class="item-description">Description: {{item.description}}<br></span>
                    <span class="item-end_date">End Date: {{item.end_date}}<br></span>
                    <span class="item-end_time">End Time: {{item.end_time}}<br></span>
                    <span class="item-id">Product ID: {{item.id}}<br></span>
                    <form @submit.prevent="">
                        <button class="button" @click="goToBid(item.id)">Make a Bid</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [],
            item: {},
            bids: [],
            bid: {},
            questions: [],
            answers: [],
            question: {},
            answer: {},
            user: {}
        }
    },
    mounted() {
        this.fetchItems()
    },
    methods: {
        goToBid(item_id) {
            this.$router.replace('/bid-detail/' + item_id)
        },

        async fetchItems() {
            let response = await fetch(
                "http://localhost:8000/api/items/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.items = data.items;
        },

        async fetchItem(item_id) {
            let response = await fetch(
                "http://localhost:8000/api/item/" + String(item_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.item = data.item;
        },

        async bidItem(item_id) {
            var obj = {item: item_id, amount: this.bidAmount};
            let response = await fetch('http://localhost:8000/api/bid/', 
            {
                method: "post",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(obj)
            }
            );
            let data = await response.json();
            this.bid = data.bid;
        },

        async fetchBids(item_id) {
            let response = await fetch(
                "http://localhost:8000/api/bids/" + String(item_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.bids = data.bids;
        },
        async fetchQuestions(item_id) {
            let response = await fetch(
                "http://localhost:8000/api/questions/" + String(item_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.questions = data.questions;
        },
        async fetchAnswers(question_id) {
            let response = await fetch(
                "http://localhost:8000/api/answers/" + String(question_id) + "/",
                {
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                }
                );
            let data = await response.json();
            this.answers = data.answers;
        },

        async sendQuestion(item_id) {
            var obj = {item: item_id, question: this.questionText};
            let response = await fetch('http://localhost:8000/api/question/', 
            {
                method: "post",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(obj)
            }
            );
            let data = await response.json();
            this.question = data.question;
        },
        async sendAnswer(item_id, question_id) {
            var obj = {item: item_id, question: question_id, answer: this.answerText};
            let response = await fetch('http://localhost:8000/api/answer/', 
            {
                method: "post",
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(obj)
            }
            );
            let data = await response.json();
            this.answer = data.answer;
        },

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

        sliceString(string) {
            string = String(string);
            var result = string.substring(string.lastIndexOf("/"));
            return result;
        }
    }
}

</script>