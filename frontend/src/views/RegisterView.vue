<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <main class="form-signin">
        <form>
            <h1 class="h3 mb-3 fw-normal">Пожалуйста зарегистрируйтесь</h1>
            <h5>Уже есть аккаунт?</h5>
            <RouterLink to="/" class="btn btn-sm btn-primary mb-3" type="submit">Войти</RouterLink>
            
            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput" placeholder="Username">
                <label for="floatingInput">Логин</label>
            </div>
            <div class="form-floating mb-2">
                <input type="email" class="form-control" id="floatingInput" placeholder="ex@mple.com">
                <label for="floatingInput">Email</label>
            </div>
            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput2" placeholder="Иванов Иван Иванович">
                <label for="floatingInput2">Фио</label>
            </div>
            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput3" placeholder="+7(XXX)-XXX-XX-XX">
                <label for="floatingInput3">Номер телефона</label>
            </div>
            <div class="form-floating mb-2">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Пароль</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="submit">Зарегистрироваться</button>
            <p class="mt-5 mb-3 text-muted text-center">© 2024</p>
        </form>
    </main>
</template>

<style></style>