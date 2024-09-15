<script lang="ts">
    import { CreateTaskRequestFromJSON, DefaultApi, type Category } from '$lib/api';
    import CategoryTooltip from '$lib/components/CategoryTooltip.svelte'; // Adjust the path as needed
    import { CreateTaskRequest } from '$lib/api';
  
    let description = '';
    let points = 0;
    let enabled = true;
    let selectedCategories: any[] = [];
  
    // Assume categories is an array of available categories fetched from the API or defined elsewhere
    export let categories: Category[] = [];
  
    export let onTaskCreated: (task: any) => void;
  
    async function handleCreateTask() {
      const newTask = {
        description,
        points,
        enabled,
        categories: selectedCategories // Now an array of IDs
      };
  
      try {
        const defaultApi = new DefaultApi();
        const newTaskRequest: CreateTaskRequest = CreateTaskRequestFromJSON(newTask);
        console.log("Attempting to create task:", newTask);
        const createdTask = await defaultApi.createTask({ createTaskRequest: newTaskRequest });
        onTaskCreated(createdTask); // Notify parent component about the new task
        resetForm();
      } catch (error) {
        console.error('Error creating task:', error);
      }
    }
  
    function resetForm() {
      description = '';
      points = 0;
      enabled = true;
      selectedCategories = [];
    }
  
    function onCategoryChange(newSelectedCategories: any[]) {
      selectedCategories = newSelectedCategories.map((cat) => cat.id);
    }
  </script>
  
  <style>
    .create-task-form {
      display: flex;
      flex-direction: column;
      gap: 15px;
      max-width: 500px;
      margin: 20px auto;
    }
  
    .create-task-form label {
      font-weight: bold;
      margin-bottom: 5px;
    }
  
    .create-task-form input[type="text"],
    .create-task-form input[type="number"] {
      padding: 8px;
      font-size: 1rem;
      width: 100%;
      box-sizing: border-box;
    }
  
    .create-task-form input[type="checkbox"] {
      margin-right: 10px;
    }
  
    .categories-list {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }
  
    .category-item {
      display: flex;
      align-items: center;
    }
  
    .create-task-form button {
      padding: 10px 20px;
      font-size: 1rem;
      cursor: pointer;
      border-radius: 4px;
      border: none;
      background-color: #28a745;
      color: white;
    }
  
    .create-task-form button:hover {
      background-color: #218838;
    }
  </style>
  
  <form class="create-task-form" on:submit|preventDefault={handleCreateTask}>
    <div>
      <label for="description">Description:</label>
      <input
        type="text"
        id="description"
        bind:value={description}
        required
      />
    </div>
  
    <div>
      <label for="points">Points:</label>
      <input
        type="number"
        id="points"
        bind:value={points}
        min="0"
        required
      />
    </div>
  
    <div>
      <label>
        <input
          type="checkbox"
          bind:checked={enabled}
        />
        Enabled
      </label>
    </div>
  
    <div>
      <label>Categories:</label>
      <CategoryTooltip categoriesList={categories} initialSelectedCategories={selectedCategories} isEditing={true} onCategoriesChange={onCategoryChange} />
    </div>
  
    <button type="submit">Create Task</button>
  </form>
  