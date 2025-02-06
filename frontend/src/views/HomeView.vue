<script setup>
import { ref } from 'vue'
import { useUsers } from '@/composables/useUsers'
import TableComponent from '@/components/TableComponent.vue'
import UserFormComponent from '@/components/UserFormComponent.vue'

const { users } = useUsers()
const user = ref()
const dialog = ref(false)
const columns = ref([
  { key: 'name', label: 'Name' },
  { key: 'email', label: 'Email' },
  { key: 'phone', label: 'Phone' },
  { key: 'created_at', label: 'Created At' },
  { key: 'street', label: 'Street' },
  { key: 'city', label: 'city' },
  { key: 'state', label: 'state' },
  { key: 'zip_code', label: 'zipcode' },
])

const showForm = (selectedUser) => {
  user.value = selectedUser
  dialog.value = true
}
</script>

<template>
  <!-- :edit="true" :remove="true" to add actions -->
  <TableComponent :items="users" :columns="columns" :edit="true" @edit="showForm" />

  <UserFormComponent v-if="user && dialog" :user="user" @close="dialog = false" :dialog="dialog" />
</template>
