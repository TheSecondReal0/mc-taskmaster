<script lang="ts">
    import '../lib/api/index'
	import { DefaultApi, type GetTasks200Response } from '../lib/api/index';

  import TaskTable from '$lib/components/TaskTable.svelte';
    
    // Dummy data for the table
    let tasks: any = [
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

  </script>
  
  <style>
    /* General page styling */
    .container {
      max-width: 800px;
      margin: 2rem auto;
      padding: 1.5rem;
      background-color: #f9f9f9;
      border-radius: 12px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
  
    .button-container {
      margin-top: 2rem;
      display: flex;
      justify-content: space-between;
    }
  
    button {
      padding: 10px 20px;
      font-size: 1rem;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  
    button.submit {
      background-color: #28a745;
      color: white;
    }
  
    button.submit:hover {
      background-color: #218838;
    }
  
    button.revert {
      background-color: #dc3545;
      color: white;
    }
  
    button.revert:hover {
      background-color: #c82333;
    }
  
    /* Responsive design */
    @media (max-width: 600px) {
      th, td {
        padding: 10px;
        font-size: 0.85rem;
      }
  
      h1 {
        font-size: 1.5rem;
      }
  
      button {
        font-size: 0.9rem;
        padding: 8px 15px;
      }
    }
  </style>

<!-- <meta http-equiv="Content-Security-Policy" content="script-src 'self' 'unsafe-eval';"> -->
  
  <div class="container">
    <TaskTable {tasks}>
    </TaskTable>
  </div>
  