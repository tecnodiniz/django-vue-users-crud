<template>
  <v-btn>Olá</v-btn>

  <div v-for="user in users" :key="user.id">
    <v-list-item>
      {{ user.name }}
    </v-list-item>
  </div>
</template>

<script setup>
defineProps({
  users: {
    type: Array,
    required: true,
  },
})
</script>
