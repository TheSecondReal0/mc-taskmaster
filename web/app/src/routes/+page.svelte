<script lang="ts">
    import '../lib/api/index'
	import { DefaultApi } from '../lib/api/index';
    
    // Dummy data for the table
    let originalData = [
      { id: 1, name: 'Alice', age: 25, job: 'Engineer' },
      { id: 2, name: 'Bob', age: 30, job: 'Designer' },
      { id: 3, name: 'Charlie', age: 28, job: 'Developer' },
    ];
  
    let data = structuredClone(originalData); // Clone data for editing
  
    function submitChanges() {
      // In a real application, this would be where you send data to the server
      console.log('Submitting changes:', data);
      originalData = structuredClone(data); // Update original data with current edits
      alert('Changes submitted successfully!');

      console.log("sending API request bruh pls")
      let defaultApi: DefaultApi = new DefaultApi();
      console.log(defaultApi.getTasksRaw());
    }
  
    function revertChanges() {
      data = structuredClone(originalData); // Revert data to original state
      alert('Changes reverted!');
      console.log("bruh bruh bruh");
    }

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
  
    h1 {
      text-align: center;
      font-size: 2rem;
      margin-bottom: 1rem;
      color: #333;
    }
  
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1rem;
    }
  
    thead {
      background-color: #007bff;
      color: white;
    }
  
    th, td {
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid #ddd;
    }
  
    th {
      text-transform: uppercase;
      font-size: 0.85rem;
    }
  
    tbody tr:nth-child(even) {
      background-color: #f2f2f2;
    }
  
    tbody tr:hover {
      background-color: #e9f5ff;
    }
  
    td {
      font-size: 0.95rem;
      color: #555;
    }
  
    input[type="text"] {
      width: 100%;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 4px;
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
  
  <div class="container">
    <h1>User Information</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Age</th>
          <th>Job</th>
        </tr>
      </thead>
      <tbody>
        {#each data as row, index}
          <tr>
            <td>{row.id}</td>
            <td>
              <input
                type="text"
                bind:value={data[index].name} />
            </td>
            <td>
              <input
                type="text"
                bind:value={data[index].age} />
            </td>
            <td>
              <input
                type="text"
                bind:value={data[index].job} />
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  
    <div class="button-container">
      <button class="submit" on:click={submitChanges}>Submit Changes</button>
      <button class="revert" on:click={revertChanges}>Revert Changes</button>
    </div>
  </div>
  