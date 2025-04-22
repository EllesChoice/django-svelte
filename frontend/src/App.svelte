<script>

  let items = [];

  // Function to fetch data from the Django backend
  const fetchItems = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/items/');
      if (res.ok) {
        items = await res.json();  // Parse the JSON data into the `items` array
      } else {
        console.error('Failed to fetch items');
      }
    } catch (err) {
      console.error('Error fetching data:', err);
    }
  };

  // Fetch items when the component mounts
  fetchItems();
  </script>

<main>
  <h1>Todo List</h1>
  <ul>
    {#each items as item}
      <li>{item.name} - {item.done ? '✅' : '❌'}</li>
    {/each}
  </ul>
</main>

<style>


</style>
