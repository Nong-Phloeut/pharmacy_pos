<template>
  <v-container>
    <v-row class="mb-4">
      <v-col cols="6">
        <v-row>
          <v-col cols="4" class="font-weight-bold">SALES PERSON</v-col>
          <v-col cols="8">{{ firstSalespersonName }}</v-col> 
        </v-row>
        <v-row>
          <v-col cols="4" class="font-weight-bold">DATE</v-col>
          <v-col cols="8">{{ formattedDate }}</v-col>
        </v-row>
      </v-col>
      
      <v-col cols="6" class="text-right">
        <v-row>
          <v-col cols="6" class="font-weight-bold">SALES AMOUNT</v-col>
          <v-col cols="6">{{ formatCurrency(dailySales.total_sales - totalTax) }}</v-col>
        </v-row>
        <v-row>
          <v-col cols="6" class="font-weight-bold">SALES TAX</v-col>
          <v-col cols="6">{{ formatCurrency(totalTax) }}</v-col>
        </v-row>
        <v-row>
          <v-col cols="6" class="font-weight-bold">SALES TOTAL</v-col>
          <v-col cols="6" class="text-h6 font-weight-bold">{{ formatCurrency(dailySales.total_sales) }}</v-col>
        </v-row>
      </v-col>
    </v-row>

    <v-row class="mb-4">
      <v-col cols="12">
        <v-menu v-model="menu" :close-on-content-click="false" location="start">
          <template #activator="{ props }">
            <v-btn color="primary" v-bind="props">
              <v-icon left>mdi-calendar-range</v-icon>
              Select Date
            </v-btn>
          </template>
          <v-date-picker v-model="selectedDate" @update:model-value="onDateChange"></v-date-picker>
        </v-menu>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <v-card>
          <v-data-table
            :headers="salesHeaders"
            :items="dailySales.sales || []"
            :items-per-page="10"
          >
            <template #item.price="{ item }">
              {{ formatCurrency(item.price) }}
            </template>
            <template #item.amount="{ item }">
              {{ formatCurrency(item.amount) }}
            </template>
            <template #item.taxRate="{ item }">
              {{ item.taxRate ? `${item.taxRate * 100}%` : '0%' }}
            </template>
            <template #item.tax="{ item }">
              {{ formatCurrency(item.tax) }}
            </template>
            <template #item.total="{ item }">
              {{ formatCurrency(item.total_sales) }}
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useReportStore } from '../stores/reportStore'

const menu = ref(false)
const selectedDate = ref(new Date())
const reportStore = useReportStore()

// --- Computed Properties ---

const dailySales = computed(() => reportStore.dailySales)

const formattedDate = computed(() => {
  if (!dailySales.value.date) return 'N/A'
  // Create a date object from the YYYY-MM-DD string to format it
  const dateObj = new Date(dailySales.value.date)
  return new Intl.DateTimeFormat('en-US', { day: '2-digit', month: '2-digit', year: '2-digit' }).format(dateObj)
})

// This assumes your API will return a `sold_by` name, not just an ID
const firstSalespersonName = computed(() => {
  // Logic to get the salesperson name. This is a placeholder.
  // You would likely get this from your store or another lookup.
  return dailySales.value.sales && dailySales.value.sales.length > 0 ? 'John Doe' : 'N/A'
})

const salesHeaders = [
  { title: 'ITEM NUMBER', key: 'itemNumber' },
  { title: 'ITEM NAME', key: 'itemName' },
  { title: 'PRICE', key: 'price' },
  { title: 'QTY', key: 'qty' },
  { title: 'AMOUNT', key: 'amount' },
  { title: 'TAX RATE', key: 'taxRate' },
  { title: 'TAX', key: 'tax' },
  { title: 'TOTAL', key: 'total_amount' },
]


const totalTax = computed(() => {
  // Summing up the tax from all items
  // return allSoldItems.value.reduce((sum, item) => sum + item.tax, 0);
});

// --- Functions ---

function formatCurrency(value) {
  if (typeof value !== 'number') return '$0.00'
  return `$${value.toFixed(2)}`
}

function onDateChange(newDate) {
  menu.value = false
  if (newDate) {
    // The date-picker gives a Date object, we need to convert it to a simple date string
    const dateString = newDate.toISOString().split('T')[0];
    reportStore.fetchDailySales(dateString)
  }
}

// Fetch sales on component mount
onMounted(() => {
  const today = new Date().toISOString().split('T')[0];
  reportStore.fetchDailySales(today)
})
</script>