// javascript used to create and update cards for each section of the dashboard

const connectorSection = document.getElementById("connectors");
const deviceSection = document.getElementById("devices");
const userSection = document.getElementById("users");
const resourceSection = document.getElementById("resources");
const serviceAccountsSection = document.getElementById("service_accounts");

function updateCards(section, newData) {
  // Get all existing cards in the section
  const existingCards = section.querySelectorAll(".card");

  // Loop through the new data and update or create cards as needed
  for (const newDataItem of newData) {
    // Check if a card already exists for this data item
    let existingCard = null;
    for (const card of existingCards) {
      if (card.dataset.id === newDataItem.id) {
        existingCard = card;
        break;
      }
    }
    // If a card already exists, update it with the new data
    if (existingCard) {
      // Loop through all fields in the data and update the corresponding elements in the card
      updateCardFields(existingCard, newDataItem);
    }

    // If no card exists for this data item, create a new one
    else {
      // Create a new card element
      const newCard = document.createElement("div");
      if (section.id === "connectors") {
          if (newDataItem.state === "ALIVE") {
              newCard.classList.add("card" ,"card-good");
          } else {
              newCard.classList.add("card", "card-bad");
          }
      } else if (section.id === "devices") {
          if (newDataItem.isTrusted === true) {
              newCard.classList.add("card", "card-good");
          } else {
              newCard.classList.add("card", "card-bad");
          }
      } else if (section.id === "users") {
          if (newDataItem.state === "ACTIVE") {
              newCard.classList.add("card", "card-good");
          } else {
              newCard.classList.add("card", "card-bad");
          }
      } else if (section.id === "service_accounts") { // this check doesn't actually work, the SA data doesn't return isActive, there's nothing in it that's good for doing a good/bad check
          if (newDataItem.isActive === true) {
              newCard.classList.add("card", "card-good");
          } else {
              newCard.classList.add("card", "card-bad")
          }
      } else if (section.id === "resources") {
          if (newDataItem.isActive === true) {
              newCard.classList.add("card", "card-good");
          } else {
              newCard.classList.add("card", "card-bad");
          }
      }
      else {
          newCard.classList.add("card");
      }

      // Loop through all fields in the data and create corresponding elements in the card
      for (const [key, value] of Object.entries(newDataItem)) {
        const fieldElement = document.createElement("div");
        fieldElement.classList.add("card-field");
        fieldElement.dataset.field = key;
        fieldElement.innerHTML = formatData(key, value);
        newCard.appendChild(fieldElement);
      }

      // Add the card to the section
      section.appendChild(newCard);
    }
  }

  // Loop through all existing cards and remove any that don't exist in the new data
  for (const card of existingCards) {
    const existingDataIds = newData.map(item => item.id);
    if (!existingDataIds.includes(card.dataset.id)) {
      card.remove();
    }
  }
}
// update card fields if data changed
function updateCardFields(card, dataItem) {
  for (const [key, value] of Object.entries(dataItem)) {
    const element = card.querySelector(`[data-field="${key}"]`);
    if (element) {
      if (typeof value === "object" && value !== null) {
        updateCardFields(element, value); // Recursively update nested objects
      } else {
        element.innerHTML = "<b>" + key + ": </b>" + value;
      }
    }
  }
}

// formats data in the card
function formatData(key, value) {
    if (typeof(value) === 'object' && value !== null) {
        console.log(value)
        for (const [key, value2] of Object.entries(value)) {
            formatData(key, value2);
        }
    } else {
        return '<b>' + key + ': </b>' + value;
    }
}

// Fetch new data for each section
function fetchDataAndUpdateCards() {
  console.log("fetching data")
  fetch("/connectors")
    .then(response => response.json())
    .then(data => updateCards(connectorSection, data));

  fetch("/devices")
    .then(response => response.json())
    .then(data => updateCards(deviceSection, data));

  fetch("/users")
    .then(response => response.json())
    .then(data => updateCards(userSection, data));

  fetch("/service_accounts")
    .then(response => response.json())
    .then(data => updateCards(serviceAccountsSection, data));

  fetch("/resources")
    .then(response => response.json())
    .then(data => updateCards(resourceSection, data));
}

// Initial fetch and update
fetchDataAndUpdateCards();

// Periodically fetch and update
setInterval(fetchDataAndUpdateCards, 60000);