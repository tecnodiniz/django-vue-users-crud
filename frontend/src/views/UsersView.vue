<script setup>
import { ref } from 'vue'
import { useUsers } from '@/composables/useUsers'
import TableComponent from '@/components/TableComponent.vue'

const { users } = useUsers()
const columns = ref([
  { key: 'name', label: 'Name' },
  { key: 'email', label: 'Eame' },
  { key: 'created_at', label: 'Created At' },
  { key: 'street', label: 'Street' },
  { key: 'city', label: 'city' },
  { key: 'state', label: 'state' },
  { key: 'zip_code', label: 'zipcode' },
])
</script>

<template>
  <TableComponent :items="users" :columns="columns" />
</template>
