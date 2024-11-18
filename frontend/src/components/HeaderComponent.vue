<script setup>
import { RouterLink } from 'vue-router'
import { ref, onMounted } from 'vue'


const state = ref(false)
const username = ref()

const getCurrentUrl = () => {
    const url = window.location.pathname
    if (url == '/register' || url == '/') {
        state.value = false
    } else {
        state.value = true
        username.value = localStorage.getItem('username')
    }
}

onMounted (()=>{
    getCurrentUrl()
})

</script>

<template>

    <div class="container">
        <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
            <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                <span class="fs-4">Cleaning "Мой Не Сам"</span>
            </a>

            <ul class="nav nav-pills" v-if="state == true">
                <li class="nav-item">
                    <RouterLink to="/home" class="nav-link">Главная</RouterLink>
                </li>
                <li class="nav-item">
                    <RouterLink to="/createOrder" class="nav-link">Оставить заявку</RouterLink>
                </li>
                <li class="nav-item d-flex align-items-center ms-5">
                    <p class="my-0">{{ username }}</p>
                </li>

            </ul>

            <!-- <button type="button" class="btn btn-primary" @click="getCurrentUrl">click</button> -->
        </header>
    </div>


</template>

<style scoped></style>
