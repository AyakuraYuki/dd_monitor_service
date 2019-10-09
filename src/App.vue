<template>
    <div id="app">
        <nav-menu/>
        <router-view/>
    </div>
</template>

<style>

</style>

<script>
    import NavMenu from "./components/NavMenu"

    export default {
        components: {
            NavMenu
        },
        methods: {}
    }
</script>
