<template>
  <TableComponent :items="users" :columns="columns" />
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { get_users } from '@/services/api'
import TableComponent from './TableComponent.vue'

const users = ref([])
const columns = ref([
  { key: 'name', label: 'Name' },
  { key: 'email', label: 'Eame' },
  { key: 'created_at', label: 'Created At' },
])

const getUsers = () => {
  get_users()
    .then((response) => {
      users.value = response.data.map((user) => ({
        ...user,
        created_at: formatDate(user.created_at),
      }))
    })
    .catch((error) => console.log(error))
}

const formatDate = (isoDate) => {
  return new Date(isoDate).toLocaleDateString('en-US', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    timeZone: 'UTC',
  })
}

onMounted(getUsers)
</script>
