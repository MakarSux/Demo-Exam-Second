<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <main class="form-signin">
        <form>
            <h1 class="h3 mb-3 fw-normal">Пожалуйста войдите</h1>
            <h5>Если вы ещё не зарегистрировались?</h5>
            <RouterLink to="/register" class="btn btn-sm btn-primary mb-3" type="submit">Регистрация</RouterLink>
            
            <div class="form-floating mb-2">
                <input type="text" class="form-control" id="floatingInput" placeholder="Username">
                <label for="floatingInput">Логин</label>
            </div>
            <div class="form-floating mb-2">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Пароль</label>
            </div>

            <button class="w-100 btn btn-lg btn-primary" type="submit">Войти</button>
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