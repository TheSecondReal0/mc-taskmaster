<script lang="ts">
    // Dummy data for the table
    let data = [
      { id: 1, name: 'Alice', age: 25, job: 'beach' },
      { id: 1, name: 'Alice', age: 25, job: 'Engineer' },
    { id: 2, name: 'Bob', age: 30, job: 'Designer' },
    { id: 3, name: 'Charlie', age: 28, job: 'Developer' },
  ];
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

  /* Responsive design */
  @media (max-width: 600px) {
    th, td {
      padding: 10px;
      font-size: 0.85rem;
    }

    h1 {
      font-size: 1.5rem;
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
      {#each data as row}
        <tr>
          <td>{row.id}</td>
          <td>{row.name}</td>
          <td>{row.age}</td>
          <td>{row.job}</td>
        </tr>
      {/each}
    </tbody>
  </table>
</div>

  