<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const user = ref({
    login: "",
    password: ""
})

const csrfToken = ref(null)

const router = useRouter()

const url = 'http://127.0.0.1:8000/'

onMounted( () => {
    getCsrfToken()
})

const getCsrfToken = () => {
    try {
        axios
            .get(`${url}get-csrf-token/`)
            .then(response => {
                csrfToken.value = response.data.csrfToken
                console.log(response.data.csrfToken)
            })

    } catch (error) {
        console.log(error)
    }
}

const login = () => {
    console.log(csrfToken.value)
    const sendData = {
        'username': user.value.login,
        'password': user.value.password,
        'csrfmiddlewaretoken': csrfToken.value
    }

    axios
        .post(`${url}api-auth/login/`, sendData, {
            headers: {
                'Content-Type': 'application/json',
                // 'X-CSRFToken': csrfToken.value
            }
        })
        .then(response => {
            console.log(response.data)
            if (response.status === 201) {
                router.push('/home')
            }
        })
        .catch(error => console.log(error))
}

</script>

<template>
    <main class="form-signin">
        <form>
            <h1 class="h3 mb-3 fw-normal">Пожалуйста войдите</h1>
            <h5>Если вы ещё не зарегистрировались?</h5>
            <RouterLink to="/register" class="btn btn-sm btn-primary mb-3" type="submit">Регистрация</RouterLink>

            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput" placeholder="Username" v-model="user.login">
                <label for="floatingInput">Логин</label>
            </div>
            <div class="form-floating mb-2">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password"
                    v-model="user.password">
                <label for="floatingPassword">Пароль</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="button" @click="login()">Войти</button>
            <p class="mt-5 mb-3 text-muted text-center">© 2024</p>
        </form>
    </main>
</template>

<style>
.form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: auto;
}
</style>