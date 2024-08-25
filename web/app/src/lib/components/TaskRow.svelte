<script lang="ts">
    export let task: any;
  
    function handleEdit() {
      console.log(`Editing task: ${task.id}`);
      // Your edit logic here
    }
  
    function handleDelete() {
      console.log(`Deleting task: ${task.id}`);
      // Your delete logic here
    }
  </script>
  
  <style>
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
  </style>
  
  <tr>
    <td>{task.id}</td>
    <td>{task.description}</td>
    <td>{task.points}</td>
    <td>{task.enabled ? 'Yes' : 'No'}</td>
    <td>
      {#each task.categories as category}
        <div>
          <strong>{category.name}</strong>
          <div class="category-info">{category.description}</div>
        </div>
      {/each}
    </td>
    <td class="row-actions">
      <button class="edit" on:click={handleEdit}>Edit</button>
      <button class="delete" on:click={handleDelete}>Delete</button>
    </td>
  </tr>
  