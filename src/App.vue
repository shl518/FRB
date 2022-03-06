<template>
  <div> 
    <School/>
    <SignImage></SignImage>
  </div>
</template>

<script>
import School from './components/School'

//import SignImage from '@/components/SignImageComponent/SignImage.vue'
import SignImage from './components/SignImage'
export default {
  name:'App',
  components:{SignImage,School}

}
</script>
