<script lang="ts">
  export let isEditing: boolean = false;
  export let categoriesList: any[] = [];
  export let onCategoriesChange: (selectedCategories: any[]) => void;
  export let initialSelectedCategories: any[] = [];

  let selectedCategories: any[] = categoriesList.filter(category => initialSelectedCategories.includes(category.id));

  // Check if a category is selected
  function isCategorySelected(categoryId: any) {
    return selectedCategories.some(cat => cat.id === categoryId);
  }

  // Toggle the selection of a category
  function toggleCategory(event: any, category: any) {
    if (event.target.checked) {
      selectedCategories = [...selectedCategories, category];
    } else {
      selectedCategories = selectedCategories.filter(cat => cat.id !== category.id);
    }

    // Call the function provided by the parent
    if (onCategoriesChange) {
      onCategoriesChange(selectedCategories);
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
    margin-right: 10px;
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
    display: flex;
    flex-wrap: wrap;
  }

  .dropdown label {
    display: flex;
    align-items: center;
    margin-right: 15px;
    margin-bottom: 10px;
  }

  .dropdown label input {
    margin-right: 5px;
  }
</style>

{#if isEditing}
  <!-- Display all categories with checkboxes and tooltips -->
  <div class="dropdown">
    {#each categoriesList as category}
      <label>
        <input
          type="checkbox"
          checked={isCategorySelected(category.id)}
          on:change={(event) => toggleCategory(event, category)} />
        <div class="tooltip">
          {category.name}
          <span class="tooltiptext">{category.description}</span>
        </div>
      </label>
    {/each}
  </div>
{:else}
  <!-- Display only selected categories with tooltips -->
  <div class="categories-display">
    {#each selectedCategories as category}
      <div class="tooltip">
        {category.name}
        <span class="tooltiptext">{category.description}</span>
      </div>
    {/each}
  </div>
{/if}
