<script lang="ts">
    import TaskRow from './TaskRow.svelte'; // Adjust the path as needed
    import CreateTaskForm from './CreateTaskForm.svelte';
    import { DefaultApi, type GetCategories200Response } from '$lib/api';
  
      // Dummy data for the table
      export let tasks: any = [
      ];
      export let categories: any = [];

  // Function to fetch tasks from the API
  async function fetchTasks() {
        let taskApi: DefaultApi = new DefaultApi();
        try {
            const response = await taskApi.getTasks();
            tasks = response.tasks; // Make sure you're accessing the right property
            console.log("TASKS", tasks)
        } catch (error) {
            console.error('Error fetching tasks:', error);
        }
    }

  async function fetchCategories() {
    let taskApi: DefaultApi = new DefaultApi();
        try {
            const response: GetCategories200Response = await taskApi.getCategories();
            categories = response.tasks; // Make sure you're accessing the right property
            console.log("CATEGORIES", categories)
        } catch (error) {
            console.error('Error fetching categories:', error);
        }
  }

    // Fetch tasks when the component is mounted
    fetchTasks();
    fetchCategories();

    function addTaskToList(newTask: any) {
    tasks = [...tasks, newTask];
  }

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
        <TaskRow task={task} categoriesList={categories} onDelete={deleteTask} />
      {/each}
    </tbody>
  </table>
  <CreateTaskForm {categories} onTaskCreated={addTaskToList} />
  