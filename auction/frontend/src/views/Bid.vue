<template>
    <div >
        <h1>Item information</h1>
    </div>

    <div class="container">
            <div class="item-box" v-for="item in items" v-bind:key="item.id">
                <figure class="item-image">
                    <img v-bind:src="sliceString(item.item_image)"/>
                </figure>

                <div class="item-info">
                    <span class="item-title">{{item.title}}<br></span>
                    <span class="item-price">Starting Price: £{{item.starting_price}}<br></span>
                    <span class="item-description">Description: {{item.description}}<br></span>
                    <span class="item-end_date">End Date: {{item.end_date}}<br></span>
                    <span class="item-end_time">End Time: {{item.end_time}}<br></span>
                    <span class="item-id">Product ID: {{item.id}}<br></span>
                </div>

                <form @submit.prevent="bidItem(item.id)">
                        <div>
                            <label>Bid</label>
                            <input type="text" v-model="bidAmount" placeholder="Enter amount">
                            <input hidden placeholder="">
                            <button type="submit">Submit</button>
                        </div>
                </form>

                <form @submit.prevent="sendQuestion(1)">
                    <div>
                        <label>Question</label>
                        <input type="text" v-model="questionText" placeholder="Enter text here...">
                        <button type="submit">Submit</button>
                    </div>
                </form>
                <form @submit.prevent="sendAnswer(1, 2)">
                    <div>
                        <label>Answer</label>
                        <input type="text" v-model="answerText" placeholder="Enter text here...">
                        <button type="submit">Submit</button>
                    </div>
    </form>
            </div>
        </div>
</template>

<script>
export default {
    data() {
        return {
            item: {},
            bids: [],
            bid: {},
            questions: [],
            answers: [],
            question: {},
            answer: {},
        }
    },
    mounted() {
        this.fetchItem(item.id),
        this.fetchBids(item.id),
        this.fetchQuestions(item.id),
        this.fetchAnswers(question.id),
        this.sendQuestion(item.id),
        this.sendAnswer(item.id, question.id)
    },
    methods: {
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
        }
    }
}
</script>