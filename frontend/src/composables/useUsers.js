import { ref, onMounted } from 'vue'
import { get_users } from '@/services/api'

export function useUsers() {
  const users = ref([])

  const fetchUsers = () => {
    get_users()
      .then((response) => {
        users.value = response.data.map(({ addresses, ...user }) => ({
          ...user,
          created_at: formatDate(user.created_at),
          ...(addresses[0] || {}),
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

  onMounted(fetchUsers)

  return { users, fetchUsers }
}
