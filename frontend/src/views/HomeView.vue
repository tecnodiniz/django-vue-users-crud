<script setup>
import UsersComponent from '@/components/UsersComponent.vue'
import { get_users } from '@/services/api'
import { onMounted, ref } from 'vue'

const users = ref([])

const getUsers = () => {
  get_users().then((response) => (users.value = response.data))
}
onMounted(() => getUsers())
</script>

<template>
  <main><UsersComponent :users="users" /></main>
</template>
