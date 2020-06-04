<template>
    <div id="dashboard" class="dashboard container-fluid">
        <div class="row">
            <div id="sidebar" class="sidebar col-md-2 d-none d-md-block sidebar p-3 d-none d-lg-block">
                <b-nav vertical class="nav-pills">
                    <b-nav-item class="p-1">
                        <b-button block variant="primary" @click="fetchLinkList">Refresh</b-button>
                    </b-nav-item>
                    <b-nav-item class="p-1">
                        <!--<b-button v-b-modal.edit-link block variant="success" @click="createLink">Add Stream</b-button>-->
                        <b-button block variant="success" @click="$_edit_handleShowDialog()">
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

                <b-table striped borderless responsive="sm" :items="links" :fields="fields" head-variant="dark">
                    <template v-slot:cell(options)="link">
                        <!--<b-button v-b-modal.edit-link size="sm" class="btn-sm bg-info text-light border-0" @click="updateLink(link.item)">Edit</b-button>-->
                        <!--&nbsp;-->
                        <b-button size="sm"
                                  class="btn-sm bg-info text-light border-0"
                                  @click="$_edit_handleShowDialog(link.item)">Edit
                        </b-button>
                        &nbsp;
                        <b-button size="sm"
                                  class="btn-sm bg-danger text-light border-0"
                                  @click="deleteLink(link.item._id)">Delete
                        </b-button>
                    </template>
                </b-table>
            </main>

            <!--<modal-edit-link @update:linkList="fetchLinkList" :item="modalEdit.item" :method="modalEdit.method"/>-->
            <edit-link :show="editDetail$.show"
                       :edit="editDetail$.edit"
                       @success="fetchLinkList"
                       @close="$_edit_handleCloseDialog"/>
            <modal-save-link-by-channel @update:linkList="fetchLinkList"/>
        </div>
    </div>
</template>

<script>
    import ModalSaveLinkByChannel from "../components/dashboard/ModalSaveLinkByChannel"
    import { deleteLink, linkList } from "../api/dashboard"
    import EditMixin from "../mixin/edit"
    import EditLink from "../components/fragment/EditLink"

    export default {
        name: "Dashboard",
        components: {
            EditLink,
            ModalSaveLinkByChannel
        },
        data () {
            return {
                form: {
                    query: ''
                },

                fields: [
                    { key: 'sort', label: 'No.', sortable: true },
                    { key: 'title', label: 'Description', sortable: true },
                    { key: 'link', label: 'Link' },
                    { key: 'options', label: 'Options' }
                ],
                links: [],

                modalEdit: {
                    item: {},
                    method: ''
                }
            }
        },
        mixins: [
            EditMixin
        ],
        methods: {
            fetchLinkList () {
                linkList({ ...this.form }).then(res => {
                    let data = res.data
                    this.links = data.list
                })
            },
            deleteLink (lid) {
                deleteLink(lid).then(() => {
                    this.fetchLinkList()
                })
            },
            // editLink (item, method) {
            //     this.modalEdit.item = item
            //     this.modalEdit.method = method
            // },
            // createLink () {
            //     this.editLink(undefined, REQUEST_POST)
            // },
            // updateLink (item) {
            //     this.editLink(item, REQUEST_PUT)
            // }
        },
        mounted () {
            this.fetchLinkList()
            document.body.classList.remove('bg-dark')
        }
    }
</script>

<style scoped>

</style>
