const { createApp } = Vue

const app = createApp({
    el: '#app',
    delimiters: ['[[', ']]'],
    data () {
        return {
            isActive: false,
        }
    },
})

app.mount('#app')