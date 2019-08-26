<template>
    <div id="dashboard" class="dashboard container-fluid">
        <div class="row">
            <div id="sidebar" class="sidebar col-md-2 d-none d-md-block sidebar p-3 d-none d-lg-block">
                <b-nav vertical class="nav-pills">
                    <b-nav-item class="p-1">
                        <b-button block variant="primary" @click="fetchLinkList">Refresh</b-button>
                    </b-nav-item>
                    <b-nav-item class="p-1">
                        <b-button v-b-modal.edit-link block variant="success" @click="createLink">
                            Add Stream
                        </b-button>
                    </b-nav-item>
                    <b-nav-item class="p-1">
                        <b-button v-b-modal.add-channel block variant="info">
                            Add Channel
                        </b-button>
                    </b-nav-item>
                </b-nav>
            </div>

            <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
                <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
                    <h1 class="h2 text-muted">Stream List</h1>
                    <div class="btn-toolbar mb-2 mb-md-0">
                        <div class="btn-group mr-2">
                            <button class="btn btn-sm btn-outline-secondary d-md-none">+</button>
                        </div>
                    </div>
                </div>

                <b-table striped borderless responsive="sm" :items="linkList" :fields="fields" head-variant="dark">
                    <template slot="[options]" slot-scope="row">
                        <b-button v-b-modal.edit-link class="btn-sm bg-info text-light"
                                  @click="editLink(row.item, 'PUT')">
                            Edit
                        </b-button>
                        &nbsp;
                        <b-button class="btn-sm bg-danger text-light" @click="deleteLink(row.item._id)">
                            Delete
                        </b-button>
                    </template>
                </b-table>
            </main>

            <modal-edit-link @update:linkList="fetchLinkList" :item="modalEdit.item" :method="modalEdit.method"/>
            <modal-save-link-by-channel @update:linkList="fetchLinkList"/>
        </div>
    </div>
</template>

<script>
    import ModalEditLink from "../components/dashboard/ModalEditLink"
    import ModalSaveLinkByChannel from "../components/dashboard/ModalSaveLinkByChannel"
    import { linkList, deleteLink } from "../api/dashboard"

    export default {
        name: "Dashboard",
        components: {
            ModalEditLink,
            ModalSaveLinkByChannel
        },
        data() {
            return {
                form: {
                    query: ''
                },

                fields: {
                    title: { label: 'Description' },
                    link: { label: 'Link' },
                    options: { label: 'Options' }
                },
                linkList: [],

                modalEdit: {
                    item: {},
                    method: ''
                }
            }
        },
        methods: {
            fetchLinkList() {
                linkList({ ...this.form }).then(res => {
                    let data = res.data
                    this.linkList = data.list
                })
            },
            deleteLink(lid) {
                deleteLink(lid).then(() => {
                    this.fetchLinkList()
                })
            },
            editLink(item, method) {
                this.modalEdit.item = item
                this.modalEdit.method = method
            },
            createLink() {
                this.editLink(undefined, 'POST')
            }
        },
        mounted() {
            this.fetchLinkList()
            document.body.classList.remove('bg-dark')
        }
    }
</script>

<style scoped>

</style>
