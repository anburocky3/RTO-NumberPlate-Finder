const inputEl = document.querySelector('input');

async function getJSONData() {
  const response = await fetch('./assets/json/data.json');
  return await response.json();
}

const searchRecord = async (value) => {
  console.log('I have got this value!', value.toUpperCase());

  const jsonData = await getJSONData();

  const recordFound = jsonData.find((record) => {
    return record.code === value.toUpperCase();
  });

  const resultSectionEl = document.querySelector('#resultSection');
  if (recordFound) {
    // record exist
    resultSectionEl.classList.remove('hidden');

    // Update the UI fields
    resultSectionEl.querySelector('#query').innerText = value.toUpperCase();
    resultSectionEl.querySelector('#rto_id').innerText = recordFound.id;
    resultSectionEl.querySelector('#rto_code').innerText = recordFound.code;
    resultSectionEl.querySelector('#rto_location').innerText =
      recordFound.location;
    resultSectionEl.querySelector('#rto_type').innerText = recordFound.type;
    resultSectionEl.querySelector('#rto_district').innerText =
      recordFound.district;
  } else {
    resultSectionEl.classList.add('hidden');
  }
};

inputEl.addEventListener('keyup', (e) => {
  // check my validation here
  if (e.key === 'Enter') {
    if (inputEl.value.length > 3) {
      searchRecord(inputEl.value);
    }
  }
});
