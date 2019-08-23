<template>
    <div id="nav-menu" class="navbar navbar-expand-sm navbar-dark bg-dark">
        <b-nav class="navbar-nav mr-auto nav-pills">
            <brand/>
            <b-nav-item>
                <router-link to="/" class="nav-link">Player</router-link>
            </b-nav-item>
            <b-nav-item>
                <router-link to="/_" class="nav-link">Dashboard</router-link>
            </b-nav-item>
        </b-nav>
    </div>
</template>

<script>
    import Brand from "./Brand"

    export default {
        name: "NavMenu",
        components: {
            Brand
        }
    }
</script>

<style>
    #nav-menu a.router-link-exact-active {
        color: #24b958;
    }
</style>
