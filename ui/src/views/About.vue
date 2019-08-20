<template>
    <div class="about">
        <h1>This is an about page</h1>
        <h6>{{env}}</h6>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                env: process.env.NODE_ENV
            }
        }
    }
</script>
