<template>
  <v-table>
    <thead>
      <tr>
        <th v-for="col in columns" :key="col.key" class="text-left">{{ col.label }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in items" :key="item.id">
        <td v-for="col in columns" :key="col.key">
          <slot>{{ item[col.key] }} </slot>
        </td>
      </tr>
    </tbody>
  </v-table>
</template>

<script setup>
defineProps({
  columns: {
    type: Array,
    require: true,
  },
  items: {
    type: Array,
    require: true,
  },
})
</script>
