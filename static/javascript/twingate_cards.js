     

      const connectorSection = document.getElementById("connectors");
      const deviceSection = document.getElementById("devices");
      const resourceSection = document.getElementById("resources");

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
            for (const [key, value] of Object.entries(newDataItem)) {
              const element = existingCard.querySelector(`[data-field="${key}"]`);
              if (element) {
                element.innerHTML = '<b>' + key + ': </b>' + value;
              }
            }
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
              if (typeof(value) === 'object' && value !== null) {
                for (const [key, value2] of Object.entries(value)) {
                    fieldElement.innerHTML = '<b>' + key + ': </b>' + value2;
                }
            } else {
                fieldElement.innerHTML = '<b>' + key + ': </b>' + value;
            }
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

      function fetchDataAndUpdateCards() {
        // Fetch new data for each section
        console.log("fetching data")
        fetch("/connectors")
          .then(response => response.json())
          .then(data => updateCards(connectorSection, data));

        fetch("/devices")
          .then(response => response.json())
          .then(data => updateCards(deviceSection, data));

        fetch("/resources")
          .then(response => response.json())
          .then(data => updateCards(resourceSection, data));
      }

      // Initial fetch and update
      fetchDataAndUpdateCards();

      // Periodically fetch and update
      setInterval(fetchDataAndUpdateCards, 60000);