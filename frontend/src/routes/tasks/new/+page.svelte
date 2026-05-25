<script lang="ts">
	let { data } = $props();

	import { goto } from '$app/navigation';
	import { TaskService } from '$lib/services/task-service';

	let title = $state('');
	let description = $state('');
	let status = $state(null);
	let dueDateTime = $state('');
	let errors = $state(new Map<string, string>());

	let formattedDueDateTime = $derived(dueDateTime ? `${dueDateTime}:00Z` : null);

	function validate() {
		errors = new Map();

		if (!title) {
			errors.set('title', 'Enter a title');
		}
		if (!status) {
			errors.set('status', 'Select a status');
		}
		if (!dueDateTime) {
			errors.set('due_date', 'Enter a due date and time');
		}

		return errors.size === 0;
	}

	function handleCancel() {
		goto('/tasks/all');
	}

	async function handleSubmit() {
		if (!validate()) {
			return
		};
		try {
			await TaskService.createTask({ 
				title,
				description,
				status,
				due_date: formattedDueDateTime 
			});
			goto('/tasks/all');
		} catch (error) {
			console.error('Error creating task:', error);
		}
	}
</script>

<div class="govuk-width-container">
	{#if errors.size > 0}
		<div class="govuk-error-summary" data-module="govuk-error-summary">
			<div role="alert">
				<h2 class="govuk-error-summary__title">There is a problem</h2>
				<div class="govuk-error-summary__body">
					<ul class="govuk-list govuk-error-summary__list">
						{#each errors.values() as message}
							<li>{message}</li>
						{/each}
					</ul>
				</div>
			</div>
		</div>
	{/if}
	<a href="/tasks/all/" class="govuk-back-link">Back</a>
	<div class="govuk-main-wrapper--auto-spacing" id="main-content" role="main">
		<fieldset class="govuk-fieldset">
			<legend class="govuk-fieldset__legend govuk-fieldset__legend--l">
				<h1 class="govuk-fieldset__heading">Add a new task</h1>
			</legend>
			<div class="govuk-form-group {errors.get('title') ? 'govuk-form-group--error' : ''}">
				<label class="govuk-label" for="task-title">Title</label>
				{#if errors.get('title')}
					<p class="govuk-error-message">
						<span class="govuk-visually-hidden">Error:</span>
						{errors.get('title')}
					</p>
				{/if}
				<input
					class="govuk-input {errors.get('title') ? 'govuk-input--error' : ''}"
					id="task-title"
					name="title"
					type="text"
					bind:value={title}
				/>
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
			<div class="govuk-form-group {errors.get('status') ? 'govuk-form-group--error' : ''}">
				<label class="govuk-label" for="task-status">Status</label>
				{#if errors.get('status')}
					<p class="govuk-error-message">
						<span class="govuk-visually-hidden">Error:</span>
						{errors.get('status')}
					</p>
				{/if}
				<select
					class="govuk-select {errors.get('status') ? 'govuk-select--error' : ''}"
					id="task-status"
					name="status"
					bind:value={status}
				>
					{#each data.taskStatuses as status}
						<option value={status.value}>{status.label}</option>
					{/each}
				</select>
			</div>
			<div class="govuk-form-group {errors.get('due_date') ? 'govuk-form-group--error' : ''}">
				<label class="govuk-label" for="task-due-date">Due date and time</label>
				{#if errors.get('due_date')}
					<p class="govuk-error-message">
						<span class="govuk-visually-hidden">Error:</span>
						{errors.get('due_date')}
					</p>
				{/if}
				<input
					class="govuk-input govuk-input--width-20 {errors.get('due_date')
						? 'govuk-input--error'
						: ''}"
					id="task-due-date"
					name="dueDate"
					type="datetime-local"
					bind:value={dueDateTime}
				/>
			</div>
			<div class="govuk-button-group">
				<button
					type="submit"
					class="govuk-button"
					data-module="govuk-button"
					onclick={handleSubmit}
				>
					Save
				</button>
				<button type="button" class="govuk-button govuk-button--secondary" onclick={handleCancel}>
					Cancel
				</button>
			</div>
		</fieldset>
	</div>
</div>
