<template>
  <div>
       <Transition name="slide-fade" initial>
      <div v-if="imageUploaded" key="uploaded-image">
        <img :src="imageShow" alt="Uploaded Brain Photo" />
        <h2>
          prediction is: {{ result }}
        </h2>
        <p>
          Thank you for uploading your photo.
        </p>
        <button @click="sendAgain">Send Again</button>
        <Transition name="loading" v-if="processing" appear>
          <div key="processing-message" class="processing-message">
            Processing... Please wait.
          </div>
        </Transition>
      </div>
      <div v-else key="upload-form">
        <img src="../assets/BrainAnimation.gif" class="resize-gif" alt="Brain Animation"/> 
        <h1>Upload Your Brain Photo</h1>
        <input type="file" accept="image/*" @change="handleImageUpload" />
        <p>Help us diagnose brain cancer by contributing your brain images.</p>
        <button @click="sendPhoto" :disabled="!imageSelected">Send Photo</button>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import axios from 'axios'

const imageUploaded = ref(false)
const uploadedImageUrl = ref('')
const processing = ref(false)
const imageSelected = ref(false)
const imageFile = ref(null) // Add imageFile ref to store selected file
const imageShow = ref(null)
const result = ref("")


function handleImageUpload(event) {
  imageFile.value = event.target.files[0]
  if (imageFile.value && imageFile.value.type.startsWith('image/')) {
    imageShow.value = URL.createObjectURL(imageFile.value);
    imageSelected.value = true;
  }
}

watchEffect((onInvalidate) => {
  if (imageFile.value) {
    const url = imageFile.value;
    onInvalidate(() => URL.revokeObjectURL(url));
  }
});


function sendPhoto() {
  processing.value = true
  imageUploaded.value = true

  const formData = new FormData();
  formData.append('image', imageFile.value); // Use imageFile.value to access the selected file

  axios
    .post('http://127.0.0.1:5000/predict', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then((response) => {
      result.value = response.data["prediction"]   
      processing.value = false
    })
    .catch((error)=>{
      console.log(error)
    })
}

function sendAgain() {
  imageUploaded.value = false
  imageSelected.value = false // Reset imageSelected when sending again
}
</script>

<style>
.slide-fade-enter-active, .slide-fade-leave-active {
  transition: all 0.3s ease-out;
}

.slide-fade-enter-from, .slide-fade-leave-to {
  transform: translateX(20px);
  opacity: 0;
}

.loading-enter-active, .loading-leave-active {
  transition: opacity 0.5s;
}

.loading-enter, .loading-leave-to {
  opacity: 0;
}

.processing-message {
  font-size: 16px;
  margin-top: 10px;
}

.resize-gif {
  width: 100px; /* Adjust to your preference */
  height: auto; /* This will keep the aspect ratio intact */
}
</style>
