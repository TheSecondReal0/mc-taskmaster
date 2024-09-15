<script lang="ts">
  import { CreateTaskRequestFromJSON, DefaultApi, type CreateTaskRequest, type UpdateTaskRequest } from '$lib/api';
  import CategoryTooltip from '$lib/components/CategoryTooltip.svelte'; // Adjust the path as needed

  export let task: any;
  export let categoriesList: any[];
  export let onDelete: (id: string) => void;
  
  let isEditing = false; // Track if the row is in edit mode
  let selectedCategories = task.categories.map(cat => cat.id); // Track selected categories
  let showDeleteConfirmation = false; // Track if the delete confirmation dialog is shown

  async function handleEdit() {
    if (isEditing) {
      const taskWithoutId = {...task}
      delete taskWithoutId.id;
      taskWithoutId.categories = selectedCategories;

      const taskRequest: CreateTaskRequest = CreateTaskRequestFromJSON(taskWithoutId);
      const updateTaskRequest: UpdateTaskRequest = {
        taskId: task.id,
        createTaskRequest: taskRequest
      }

      console.log("ATTEMPTING TO UPDATE TASK", updateTaskRequest);

      try{
        const defaultApi = new DefaultApi();
        await defaultApi.updateTask(updateTaskRequest);
      } catch (error) {
        console.error('Error updating task:', error);
      }
    }

    isEditing = !isEditing; // Toggle edit mode
  }

  function onCategoriesChange(newSelectedCategories: any[]){
    selectedCategories = newSelectedCategories.map(cat => cat.id);
  }

  function confirmDelete() {
    showDeleteConfirmation = true;
  }

  function cancelDelete() {
    showDeleteConfirmation = false;
  }

  async function proceedDelete() {
    try {
      const defaultApi = new DefaultApi();
      await defaultApi.deleteTask({ taskId: task.id }); // Replace with your API call
      onDelete(task.id); // Trigger the parent to remove the deleted task from the list
    } catch (error) {
      console.error('Error deleting task:', error);
    } finally {
      showDeleteConfirmation = false;
    }
  }
</script>

<style>
  tr {
    border-bottom: 1px solid #ddd;
    background-color: #f9f9f9;
  }

  tr:nth-child(even) {
    background-color: #f2f2f2;
  }

  tr:hover {
    background-color: #e9f5ff;
  }

  td {
    padding: 12px;
    vertical-align: middle;
    font-size: 0.95rem;
    color: #555;
  }

  .row-actions {
    display: flex;
    gap: 10px;
  }

  button {
    padding: 5px 10px;
    font-size: 0.85rem;
    cursor: pointer;
    border-radius: 4px;
    border: none;
  }

  button.edit {
    background-color: #007bff;
    color: white;
  }

  button.delete {
    background-color: #dc3545;
    color: white;
  }

  button.edit:hover {
    background-color: #0056b3;
  }

  button.delete:hover {
    background-color: #c82333;
  }

  input[type="text"], input[type="checkbox"] {
    padding: 5px;
    font-size: 0.85rem;
  }

  /* Styles for the confirmation dialog */
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .modal {
    background: white;
    padding: 20px;
    border-radius: 5px;
    text-align: center;
  }

  .modal p {
    margin-bottom: 20px;
  }

  .modal button {
    margin: 0 10px;
    padding: 5px 15px;
    font-size: 0.85rem;
  }

  .modal button.confirm {
    background-color: #dc3545;
    color: white;
  }

  .modal button.cancel {
    background-color: #6c757d;
    color: white;
  }
</style>

<tr>
  <!-- Task ID field is not editable -->
  <td>{task.id}</td>
  
  <!-- Description field: switches between text input and plain text -->
  <td>
    {#if isEditing}
      <input type="text" bind:value={task.description} />
    {:else}
      {task.description}
    {/if}
  </td>
  
  <!-- Points field: switches between text input and plain text -->
  <td>
    {#if isEditing}
      <input type="text" bind:value={task.points} />
    {:else}
      {task.points}
    {/if}
  </td>
  
  <!-- Enabled field: switches between checkbox and plain text -->
  <td>
    {#if isEditing}
      <input type="checkbox" bind:checked={task.enabled} />
    {:else}
      {task.enabled ? 'Yes' : 'No'}
    {/if}
  </td>
  
  <!-- Categories field uses the CategoryTooltip component -->
  <td>
    <CategoryTooltip categoriesList={categoriesList} initialSelectedCategories={selectedCategories} isEditing={isEditing} onCategoriesChange={onCategoriesChange} />
  </td>
  
  <!-- Edit/Delete buttons -->
  <td class="row-actions">
    <button class="edit" on:click={handleEdit}>
      {isEditing ? 'Save' : 'Edit'}
    </button>
    <button class="delete" on:click={confirmDelete}>Delete</button>
  </td>
</tr>

{#if showDeleteConfirmation}
  <div class="modal-overlay">
    <div class="modal">
      <p>Are you sure you want to delete this task?</p>
      <button class="confirm" on:click={proceedDelete}>Yes</button>
      <button class="cancel" on:click={cancelDelete}>No</button>
    </div>
  </div>
{/if}
