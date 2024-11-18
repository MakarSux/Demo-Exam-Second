<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios';

const orders = ref([])
const usernamE = ref('')
const userId = ref(null)
const isAdmin = ref(false)
const url = 'http://127.0.0.1:8000/'

const getOrders = () => {
    axios
        .get(`${url}orders/`)
        .then(response => {
            orders.value = response.data
            usernamE.value = localStorage.getItem('username')
            userId.value = parseInt(localStorage.getItem('user_id'), 10)
            isAdmin.value = localStorage.getItem('admin') === 'true'
        })
        .catch(error => {
            console.error('Ошибка при получении заказов:', error)
        })
}

const filteredOrders = computed(() => {
    return orders.value.filter(el => el.client === userId.value || isAdmin.value)
})

onMounted(() => {
    getOrders()
})
</script>

<template>
    <h2>Список заявок</h2>

    <div class="container text-center">
        <div class="row py-2">
            <div class="col">
                <b>Адрес</b>
            </div>
            <div class="col">
                <b> Предпочитительная дата </b>
            </div>
            <div class="col">
                <b> Предпочитительное время</b>
            </div>
            <div class="col">
                <b> Вид услуги/Сервис</b>
            </div>
            <div class="col">
                <b> Тип оплаты</b>
            </div>
        </div>
        <hr>
        <div class="row py-2" v-for="el in filteredOrders" :key="el.id">
            <div class="col">{{ el.adress }}</div>
            <div class="col">{{ el.desired_date }}</div>
            <div class="col">{{ el.desired_time }}</div>
            <div class="col">{{ el.service_kind }}</div>
            <div class="col">{{ el.payment_type }}</div>
        </div>
        <hr>
    </div>
</template>

<style scoped></style>