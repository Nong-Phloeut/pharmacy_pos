<!-- views/ExpiredItemsReport.vue -->
<template>
  <div>
    <custom-title> Expired & Expiring Items Report </custom-title>

    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title class="text-h6 font-weight-bold">Report</v-card-title>
          <v-data-table
            :headers="expiredHeaders"
            :items="expiredItems"
            items-per-page="10"
          ></v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { ref } from "vue";

const expiredHeaders = [
  { title: "Medication Name", key: "name" },
  { title: "SKU", key: "sku" },
  { title: "Expiry Date", key: "expiryDate" },
  { title: "Stock", key: "stock" },
];

const expiredItems = ref([
  { name: "Ibuprofen", sku: "IBU-987", expiryDate: "2025-07-20", stock: 15 },
  { name: "Cough Syrup", sku: "CS-012", expiryDate: "2025-08-01", stock: 8 },
  { name: "Vitamin C", sku: "VIT-345", expiryDate: "2025-09-10", stock: 50 },
]);
</script>

<style scoped>
/* No scoped styles needed */
</style>
