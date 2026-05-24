<script lang="ts">
	let { data } = $props();

	import { goto } from '$app/navigation';
	import { TaskService } from '$lib/services/task-service';

	let title = $state('');
	let description = $state('');
	let status = $state<string | null>(null);
	let dueDateTime = $state('');

    // Convert dueDateTime to ISO format with 'Z' suffix for UTC
	let dueDate = $derived(dueDateTime ? `${dueDateTime}:00Z` : null);

	function handleCancel() {
		goto('/tasks/all');
	}

	async function handleSubmit() {
		try {
			await TaskService.createTask({ title, description, status, due_date: dueDate });
			goto('/tasks/all');
		} catch (error) {
			console.error('Error creating task:', error);
		}
	}
</script>

<fieldset class="govuk-fieldset">
	<legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
		<h1 class="govuk-fieldset__heading">Add a new task</h1>
	</legend>
	<div class="govuk-form-group">
		<label class="govuk-label" for="task-title">Title</label>
		<input class="govuk-input" id="task-title" name="title" type="text" bind:value={title} />
	</div>
	<div class="govuk-form-group">
		<label class="govuk-label" for="task-description">Description (optional)</label>
		<textarea
			class="govuk-textarea"
			id="task-description"
			name="description"
			rows="5"
			bind:value={description}
		></textarea>
	</div>
	<div class="govuk-form-group">
		<label class="govuk-label" for="task-status">Status</label>
		<select class="govuk-select" id="task-status" name="status" bind:value={status}>
			{#each data.taskStatuses as status}
				<option value={status.value}>{status.label}</option>
			{/each}
		</select>
	</div>
	<div class="govuk-form-group">
		<label class="govuk-label" for="task-due-date">Due date and time</label>
		<input
			class="govuk-input govuk-input--width-20"
			id="task-due-date"
			name="dueDate"
			type="datetime-local"
			bind:value={dueDateTime}
		/>
	</div>
	<div class="govuk-button-group">
		<button type="submit" class="govuk-button" data-module="govuk-button" onclick={handleSubmit}>
			Save
		</button>
		<button type="button" class="govuk-button govuk-button--secondary" onclick={handleCancel}>
			Cancel
		</button>
	</div>
</fieldset>
