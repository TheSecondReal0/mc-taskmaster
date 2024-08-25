<script lang="ts">
	import { DefaultApi } from '$lib/api';
  import CategoryTooltip from '$lib/components/CategoryTooltip.svelte'; // Adjust the path as needed

  export let task: any;
  export let onDelete: (id: string) => void;
  
  let isEditing = false; // Track if the row is in edit mode
  let selectedCategories = task.categories.map(cat => cat.name); // Track selected categories

  function handleEdit() {
    isEditing = !isEditing; // Toggle edit mode
  }

  async function handleDelete() {
    try {
      const defaultApi = new DefaultApi;
      const response = await defaultApi.deleteTask({taskId: task.id}); // Replace with your API call
      onDelete(task.id); // Trigger the parent to remove the deleted task from the list
    } catch (error) {
      console.error('Error deleting task:', error);
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
    {#each task.categories as category}
      <CategoryTooltip {category} {isEditing} bind:selectedCategories />
    {/each}
  </td>
  
  <!-- Edit/Delete buttons -->
  <td class="row-actions">
    <button class="edit" on:click={handleEdit}>
      {isEditing ? 'Save' : 'Edit'}
    </button>
    <button class="delete" on:click={handleDelete}>Delete</button>
  </td>
</tr>
