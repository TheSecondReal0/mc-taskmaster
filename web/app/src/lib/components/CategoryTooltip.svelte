<script lang="ts">
    export let category: any;
    export let isEditing: boolean = false;
    export let selectedCategories: string[] = [];
  
    // Sample available categories for testing
    const availableCategories = ['pvp', 'fun', 'competitive'];
  
    // Check if a category is selected
    function isCategorySelected(categoryName: string) {
      return selectedCategories.includes(categoryName);
    }
  
    // Toggle the selection of a category
    function toggleCategory(event: any, categoryName: string) {
      if (event.target.checked) {
        selectedCategories = [...selectedCategories, categoryName];
      } else {
        selectedCategories = selectedCategories.filter(cat => cat !== categoryName);
      }
    }
  </script>
  
  <style>
    .tooltip {
      position: relative;
      display: inline-block;
      cursor: pointer;
      font-weight: bold;
      color: #333;
    }
  
    .tooltip .tooltiptext {
      visibility: hidden;
      width: 200px;
      background-color: #555;
      color: #fff;
      text-align: center;
      border-radius: 6px;
      padding: 5px;
      position: absolute;
      z-index: 1;
      bottom: 125%;
      left: 50%;
      margin-left: -100px;
      opacity: 0;
      transition: opacity 0.3s;
    }
  
    .tooltip:hover .tooltiptext {
      visibility: visible;
      opacity: 1;
    }
  
    .tooltip .tooltiptext::after {
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      margin-left: -5px;
      border-width: 5px;
      border-style: solid;
      border-color: #555 transparent transparent transparent;
    }
  
    .dropdown {
      position: relative;
      display: inline-block;
    }
  
    .dropdown-content {
      display: block;
      position: absolute;
      background-color: #f9f9f9;
      min-width: 200px;
      box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
      padding: 10px;
      z-index: 1;
    }
  
    .dropdown-content label {
      display: flex;
      align-items: center;
      margin-bottom: 8px;
    }
  
    .dropdown-content label input {
      margin-right: 10px;
    }
  
    .dropdown-content label:last-child {
      margin-bottom: 0;
    }
  </style>
  
  {#if isEditing}
    <!-- Dropdown menu with checkboxes for each potential category -->
    <div class="dropdown">
      <div class="dropdown-content">
        {#each availableCategories as availableCategory}
          <label>
            <input
              type="checkbox"
              checked={isCategorySelected(availableCategory)}
              on:change={(event) => toggleCategory(event, availableCategory)} />
            {availableCategory}
          </label>
        {/each}
      </div>
    </div>
  {:else}
    <!-- Default tooltip display for categories -->
    <div class="tooltip">
      {category.name}
      <span class="tooltiptext">{category.description}</span>
    </div>
  {/if}
  