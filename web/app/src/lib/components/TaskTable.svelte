<script lang="ts">
    import TaskRow from './TaskRow.svelte'; // Adjust the path as needed
  
    export let tasks: any[] = [];
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
        <TaskRow task={task} />
      {/each}
    </tbody>
  </table>
  