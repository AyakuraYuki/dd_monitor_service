import axios from 'axios'

export const BASE_API = 'http://127.0.0.1:5140/'
const api = axios.create()
api.defaults.timeout = 10000
api.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8'
api.defaults.baseURL = BASE_API

export default api

export const REQUEST_GET = 'GET'
export const REQUEST_POST = 'POST'
export const REQUEST_PUT = 'PUT'
export const REQUEST_DELETE = 'DELETE'
