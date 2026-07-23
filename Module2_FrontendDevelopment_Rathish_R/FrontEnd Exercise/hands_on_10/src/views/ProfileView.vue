<template>
  <main class="profile-view">
    <h2>Student Profile</h2>
    
    <div class="summary">
      <h3>Enrollment Summary</h3>
      <p><strong>Total Enrolled Courses:</strong> {{ enrolledCourses.length }}</p>
      <p><strong>Total Credits:</strong> {{ totalCredits }}</p>
      <button class="reset-btn" @click="store.$reset()">Reset All Enrollments</button>
    </div>

    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="enrolledCourses.length > 0" class="enrolled-list">
      <h3>Enrolled Courses</h3>
      <ul>
        <li v-for="course in enrolledCourses" :key="course.id">
          <strong>{{ course.name }}</strong> ({{ course.code }}) - {{ course.credits }} credits
          <button class="unenroll-btn" @click="store.unenroll(course.id)">Unenroll</button>
        </li>
      </ul>
    </div>
    <div v-else class="empty-state">
      <p>You are not enrolled in any courses yet.</p>
      <button @click="router.push('/courses')">Browse Courses</button>
    </div>
  </main>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'
import { useEnrollmentStore } from '../stores/enrollment'

const router = useRouter()
const store = useEnrollmentStore()

// Step 149: Use storeToRefs(store) to destructure reactive state
const { enrolledCourses, totalCredits, error } = storeToRefs(store)
</script>

<style scoped>
.profile-view {
  padding: 2rem;
}
.summary {
  background-color: #f0f8ff;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 20px;
}
.reset-btn {
  background-color: #f39c12;
  color: white;
  margin-top: 10px;
}
.reset-btn:hover {
  background-color: #e67e22;
}
.enrolled-list ul {
  list-style-type: none;
  padding: 0;
}
.enrolled-list li {
  padding: 10px;
  border-bottom: 1px solid #eee;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.unenroll-btn {
  background-color: #ff4757;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
}
.unenroll-btn:hover {
  background-color: #ff6b81;
}
.error {
  color: red;
  font-weight: bold;
  margin-bottom: 15px;
}
button {
  padding: 8px 15px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #3aa876;
}
</style>
