<script lang="ts">
    import TaskRow from './TaskRow.svelte'; // Adjust the path as needed
    import { DefaultApi } from '$lib/api';
  
      // Dummy data for the table
      export let tasks: any = [
      ];

  // Function to fetch tasks from the API
  async function fetchTasks() {
        let taskApi: DefaultApi = new DefaultApi();
        try {
            const response = await taskApi.getTasks();
            tasks = response.tasks; // Make sure you're accessing the right property
            console.log(tasks)
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    }

    // Fetch tasks when the component is mounted
    fetchTasks();

    function deleteTask(taskId: string) {
      console.log("deleting ", taskId);
      tasks = tasks.filter(task => task.id !== taskId);
    }

  </script>
  
  <table>
    <thead>
      <tr>
        <th>Task ID</th>
        <th>Description</th>
        <th>Points</th>
        <th>Enabled</th>
        <th>Categories</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      {#each tasks as task}
        <TaskRow task={task} onDelete={deleteTask} />
      {/each}
    </tbody>
  </table>
  