<script setup>
import axios from 'axios'
import { ref } from 'vue'

const address = ref('')
const desiredDate = ref('')
const desiredTime = ref('')
const serviceKind = ref('Общий клининг')
const paymentType = ref('Наличные')

const submitOrder = () => {
    const orderData = {
        adress: address.value,
        desired_date: desiredDate.value,
        desired_time: desiredTime.value,
        service_kind: serviceKind.value,
        payment_type: paymentType.value,
    }

    axios
        .post('http://127.0.0.1:8000/orders/', orderData)
        .then(response => {
            console.log('Заявка успешно отправлена:', response.data)
            // Очистка формы после успешной отправки
            address.value = ''
            desiredDate.value = ''
            desiredTime.value = ''
            serviceKind.value = 'Общий клининг'
            paymentType.value = 'Наличные'
        })
        .catch(error => {
            console.error('Ошибка при отправке заявки:', error)
        })
}
</script>

<template>
    <h1>Оставляйте свою заявку!</h1>
    <h6 class="text-secondary">после обработки данных - мы вам перезвоним!</h6>
    <main class="form-signin">
        <form>
            <div class="form-floating mb-2">
                <input v-model="address" type="text" class="form-control" id="floatingInput" placeholder="">
                <label for="floatingInput">Адрес</label>
            </div>
            <div class="form-floating mb-2">
                <input v-model="desiredDate" type="date" class="form-control" id="floatingInput" placeholder="">
                <label for="floatingInput">Предпочитительная дата</label>
            </div>
            <div class="form-floating mb-2">
                <input v-model="desiredTime" type="time" class="form-control" id="floatingInput" placeholder="">
                <label for="floatingInput">Предпочитительное время</label>
            </div>
            <div class="form-floating mb-2">
                <select v-model="serviceKind" class="form-control" id="floatingInput">
                    <option value="Общий клининг">Общий клининг</option>
                    <option value="Генеральная уборка">Генеральная уборка</option>
                    <option value="Послестроительная уборка">Послестроительная уборка</option>
                    <option value="Химчистка ковров и мебели">Химчистка ковров и мебели</option>
                </select>
                <label for="floatingInput">Вид услуги/Сервис</label>
            </div>
            <div class="form-floating mb-2">
                <select v-model="paymentType" class="form-control" id="floatingInput">
                    <option value="Наличные">Наличные</option>
                    <option value="Банковская карта">Банковская карта</option>
                </select>
                <label for="floatingInput">Тип оплаты</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="button" @click="submitOrder">Оставить заявку</button>
            <p class="mt-5 mb-3 text-muted text-center">© 2024</p>
        </form>
    </main>
</template>

<style></style>