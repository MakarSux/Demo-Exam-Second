<script setup>

import { RouterLink, useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const user = ref({
    login: "",
    email: "",
    firstName: "",
    lastName: "",
    phone: "",
    password: ""
})

const router = useRouter()
const url = 'http://127.0.0.1:8000/'

const register = () => {
    const sendData = {
        'username': user.value.login,
        'email': user.value.email,
        'first_name': user.value.firstName,
        'last_name': user.value.lastName,
        'phone': user.value.phone,
        'password': user.value.password
    }

    axios
        .post(`${url}users/`, sendData, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            console.log(response.data)
            if (response.status === 201) {
                router.push('/home')
            }
        })
        .catch (error => console.log(error))
}

</script>

<template>
    <main class="form-signin">
        <form>
            <h1 class="h3 mb-3 fw-normal">Пожалуйста зарегистрируйтесь</h1>
            <h5>Уже есть аккаунт?</h5>
            <RouterLink to="/" class="btn btn-sm btn-primary mb-3" type="submit">Войти</RouterLink>

            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput" placeholder="Username" v-model="user.login">
                <label for="floatingInput">Логин</label>
            </div>
            <div class="form-floating mb-2">
                <input type="email" class="form-control" id="floatingInput1" placeholder="ex@mple.com"
                    v-model="user.email">
                <label for="floatingInput1">Email</label>
            </div>
            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput2" placeholder="Иванов Иван Иванович"
                    v-model="user.firstName">
                <label for="floatingInput2">Имя</label>
            </div>
            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput2-1" placeholder="Иванов Иван Иванович"
                    v-model="user.lastName">
                <label for="floatingInput2-1">Фамилия</label>
            </div>
            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput3" placeholder="+7(XXX)-XXX-XX-XX"
                    v-model="user.phone">
                <label for="floatingInput3">Номер телефона</label>
            </div>
            <div class="form-floating mb-2">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password"
                    v-model="user.password">
                <label for="floatingPassword">Пароль</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="button" @click="register()">Зарегистрироваться</button>
            <p class="mt-5 mb-3 text-muted text-center">© 2024</p>
        </form>
    </main>
</template>

<style></style>