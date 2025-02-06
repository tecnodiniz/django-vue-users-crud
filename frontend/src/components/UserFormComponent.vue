<script setup>
import { ref, toRef } from 'vue'

const props = defineProps({
  user: {
    type: Object,
    default: () => ({}),
  },
  dialog: Boolean,
})

const dialog = toRef(props, 'dialog')
// const emit = defineEmits(['new-user', 'close'])

const form = ref({
  valid: false,
  name: props.user?.name || '',
  email: props.user?.email || '',
  phone: props.user?.phone || '',
  street: props.user?.street || '',
  city: props.user?.city || '',
  state: props.user?.state || '',
  zip_code: props.user?.zip_code || '',
})

const rules = ref({
  nameRules: (value) => {
    if (!value) return 'Name is required'
    if (value?.length < 2) return 'Name must have at least 2 caracters'
    return true
  },
  required: (v) => !!v || 'Field is required',
})

// const emitUser = () => {
//   if (form.value.valid) {
//     const payload = createPayload(form.value)
//     emit('new-user', payload)
//     resetForm()
//   }
// }

// const createPayload = ({ username, roles, active, password, preferences }) => ({
//   username,
//   roles,
//   active,
//   password,
//   preferences: {
//     timezone: preferences?.timezone,
//   },
// })

// const defaultForm = () => ({
//   valid: false,
//   name: '',
//   email: '',
//   phone: '',
//   street: '',
//   city: '',
//   state: '',
//   zip_code: '',
// })

// const setForm = () => ({
//   valid: false,
//   name: props.user?.name || '',
//   email: props.user?.email || '',
//   phone: props.user?.phone || '',
//   street: props.user?.street || '',
//   city: props.user?.city || '',
//   state: props.user?.state || '',
//   zip_code: props.user?.zip_code || '',
// })
// const resetForm = () => (form.value = defaultForm())
</script>
<template>
  <v-dialog v-model="dialog" max-width="600" persistent>
    <v-card prepend-icon="mdi-account" title="New User">
      <v-card-text>
        <v-form v-model="form.valid">
          <v-row dense>
            <v-col cols="12" sm="6">
              <v-text-field
                v-model="form.name"
                hint="User Name"
                label="User Name*"
                required
                :rules="[rules.nameRules]"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="form.email" label="Email" type="email"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="form.phone" label="Phone" type="text"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="form.street" label="Street" type="text"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="form.city" label="City" type="text"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="form.state" label="State" type="text"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6">
              <v-text-field v-model="form.zip_code" label="Zip Code" type="text"></v-text-field>
            </v-col>
          </v-row>
        </v-form>
        <slot></slot>

        <small class="text-caption text-medium-emphasis">*indicates required field</small>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>

        <v-btn text="Close" variant="plain" @click="$emit('close')"></v-btn>

        <v-btn :disabled="!form.valid" color="primary" text="Create" variant="tonal"></v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
