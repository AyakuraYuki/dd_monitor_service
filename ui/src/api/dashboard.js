import api from './api'

// region Link

export const linkList = ({ query }) => {
    const uri = '/_/link/list'
    return api.post(uri, { query })
}

export const simpleGetLinkList = () => {
    const uri = '/_/link/list'
    return api.get(uri)
}

export const saveLink = ({ title, link }) => {
    const uri = '/_/link/save'
    return api.post(uri, { title, link })
}

export const saveLinkByChannel = ({ title, channel }) => {
    const uri = '/_/link/save/channel'
    return api.post(uri, { title, channel })
}

export const updateLink = (linkId, { title, link, sort }) => {
    const uri = `/_/link/lid/${linkId}`
    return api.put(uri, { title, link, sort })
}

export const getLink = (linkId) => {
    const uri = `/_/link/lid/${linkId}`
    return api.get(uri)
}

export const deleteLink = (linkId) => {
    const uri = `/_/link/lid/${linkId}`
    return api.delete(uri)
}

// endregion

// region Channel

export const channelList = ({ query }) => {
    const uri = '/_/channel/list'
    return api.post(uri, { query })
}

export const simpleGetChannelList = () => {
    const uri = '/_/channel/list'
    return api.get(uri)
}

export const saveChannel = ({ name, channelId }) => {
    const uri = '/_/channel/save'
    return api.post(uri, { name, channelId })
}

export const updateChannel = (cid, { name, channelId }) => {
    const uri = `/_/channel/cid/${cid}`
    return api.put(uri, { name, channelId })
}

export const getChannel = (cid) => {
    const uri = `/_/channel/cid/${cid}`
    return api.get(uri)
}

export const deleteChannel = (cid) => {
    const uri = `/_/channel/cid/${cid}`
    return api.delete(uri)
}

// endregion
